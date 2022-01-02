
#url = http://127.0.0.1:5000/api/doc

from flask import Flask
from flask_restplus import Api
from flask import Blueprint
from flask_restplus import Namespace, Resource, fields
from sklearn.ensemble import GradientBoostingClassifier
import pandas as pd
import numpy as np
app = Flask(__name__, template_folder="templatesForms") 

blueprint = Blueprint('app', __name__ , url_prefix='/api')
api_extension = Api(
    blueprint,
    title='API NEWS POPULARITY',
    version='1.0',
    description='Application tutorial to demonstrate Flask RESTplus extension\
        for better project structure and auto generated documentation',
    doc='/doc'
)
namespace = Namespace('api_test', 'test if an article can be popular using GradientBoostingClassifier model')
app.config["RESTPLUS_MASK_SWAGGER"] = False
app.config.SWAGGER_UI_DOC_EXPANSION = "list"

hello_world_model=namespace.model("api_test", {"n_tokens_title (number)": fields.String(description="choose the number of tokens the article title"),"n_tokens_content (number)": fields.String(description="choose the number of tokens the article content"),"num_imgs (number)": fields.String(description="choose the number of images in the article"),"weekday (Monday/Tuesday/Wednesday/Thursday/Friday/Saturday/Sunday)": fields.String(description="choose the day when the article is out"),"channel (lifestyle/entertainment/bus/socmed/tech/world)": fields.String(description="choose the theme of the article")},)

@namespace.route('')
class HelloWorld(Resource):
    
    @namespace.doc(body=hello_world_model)
    def post(self):
        '''Hello world message endpoint'''
        x_test=list(namespace.payload.values()) #les valeurs des features
                
        x_test[0]=float(x_test[0])
        x_test[1]=float(x_test[1])
        x_test[2]=float(x_test[2])       
        
        if x_test[3]=="Monday":
            x_test[3]=1
        elif x_test[3]=="Tuesday":
            x_test[3]=2
        elif x_test[3]=="Wednesday":
            x_test[3]=3
        elif x_test[3]=="Thursday":
            x_test[3]=4
        elif x_test[3]=="Friday":
            x_test[3]=5
        elif x_test[3]=="Saturday":
            x_test[3]=6
        elif x_test[3]=="Sunday":
            x_test[3]=7
        else :
            x_test[3]=0
        
        if x_test[4]=="lifestyle":
            x_test[4]=1
        elif x_test[4]=="entertainment":
            x_test[4]=2
        elif x_test[4]=="bus":
            x_test[4]=3
        elif x_test[4]=="socmed":
            x_test[4]=4
        elif x_test[4]=="tech":
            x_test[4]=5
        elif x_test[4]=="world":
            x_test[4]=6
        else :
            x_test[4]=0
        
        
        x_new_test=pd.DataFrame(columns=['n_tokens_title','n_tokens_content','num_imgs','weekday','channel'])       
        df_new_row = pd.DataFrame(data=np.array([[x_test[0],x_test[1],x_test[2],x_test[3],x_test[4]]]), columns=['n_tokens_title','n_tokens_content','num_imgs','weekday','channel'])
        x_new_test = pd.concat([x_new_test,df_new_row], ignore_index=True)
        
        data=pd.read_csv('OnlineNewsPopularity.csv', sep=", ")
        pd.set_option('display.max_columns', 100)
        data.drop(data.iloc[:,38:60], inplace=True, axis=1)
        data.drop(data.iloc[:,19:31], inplace=True, axis=1)
        data.drop(data.iloc[:,10:13], inplace=True, axis=1)
        data.drop(data.iloc[:,4:9], inplace=True, axis=1)
        data.drop(data.iloc[:,0:2], inplace=True, axis=1)
        
        data['weekday']='no day'
        data.loc[data['weekday_is_monday'] ==1, 'weekday'] = 'Monday'
        data.loc[data['weekday_is_tuesday'] ==1,'weekday']='Tuesday'
        data.loc[data['weekday_is_wednesday']==1,'weekday']='Wednesday'
        data.loc[data['weekday_is_thursday']==1,'weekday']='Thursday'
        data.loc[data['weekday_is_friday']==1,'weekday']='Friday'
        data.loc[data['weekday_is_saturday']==1,'weekday']='Saturday'
        data.loc[data['weekday_is_sunday']==1,'weekday']='Sunday'
        
        data['channel']='no channel'
        data.loc[data['data_channel_is_lifestyle'] ==1, 'channel'] = 'lifestyle'
        data.loc[data['data_channel_is_entertainment'] ==1,'channel']='entertainment'
        data.loc[data['data_channel_is_bus']==1,'channel']='bus'
        data.loc[data['data_channel_is_socmed']==1,'channel']='socmed'
        data.loc[data['data_channel_is_tech']==1,'channel']='tech'
        data.loc[data['data_channel_is_world']==1,'channel']='world'
        
        data.loc[data['weekday'] == 'no day', 'weekday'] = 0
        data.loc[data['weekday'] == 'Monday', 'weekday'] = 1
        data.loc[data['weekday'] == 'Tuesday','weekday'] = 2
        data.loc[data['weekday'] == 'Wednesday','weekday'] = 3
        data.loc[data['weekday'] == 'Thursday','weekday'] = 4
        data.loc[data['weekday'] == 'Friday','weekday'] = 5
        data.loc[data['weekday'] == 'Saturday','weekday'] = 6
        data.loc[data['weekday'] == 'Sunday','weekday'] = 7
            
        data.loc[data['channel'] == 'no channel', 'channel'] = 0
        data.loc[data['channel'] == 'lifestyle', 'channel'] = 1
        data.loc[data['channel'] == 'entertainment','channel'] = 2
        data.loc[data['channel'] == 'bus','channel'] = 3
        data.loc[data['channel'] == 'socmed','channel'] = 4
        data.loc[data['channel'] == 'tech','channel'] = 5
        data.loc[data['channel'] == 'world','channel'] = 6
        
        
        
        data.drop(columns=['data_channel_is_lifestyle','data_channel_is_entertainment','data_channel_is_bus','data_channel_is_socmed','data_channel_is_tech','data_channel_is_world','weekday_is_monday','weekday_is_tuesday','weekday_is_wednesday','weekday_is_thursday','weekday_is_friday','weekday_is_saturday','weekday_is_sunday'], axis=1,inplace=True)
        
        Y = data['shares']
        X = data.drop(columns=['shares'])
        
        
        Y=np.where(Y>= 1400,1,0)
        

        modele=GradientBoostingClassifier(
                                max_features='log2',
                                learning_rate=0.1,
                                max_depth= 5,
                                min_samples_leaf= 5,
                                n_estimators=180)
        modele.fit(X,Y)
        y_pred = modele.predict(x_new_test)
        print(y_pred)
        if y_pred == 1:
            return "popular"
        else:
            return "not popular"
        
        
api_extension.add_namespace(namespace)
app.register_blueprint(blueprint)
if __name__ == "__main__":

    #Launch our Website
    print("Launch :")
    app.run()
    
