# -*- coding: UTF-8 -*-
import requests as req
import json,sys,time
#先注册azure应用,确保应用有以下权限:
#files:	Files.Read.All、Files.ReadWrite.All、Sites.Read.All、Sites.ReadWrite.All
#user:	User.Read.All、User.ReadWrite.All、Directory.Read.All、Directory.ReadWrite.All
#mail:  Mail.Read、Mail.ReadWrite、MailboxSettings.Read、MailboxSettings.ReadWrite
#注册后一定要再点代表xxx授予管理员同意,否则outlook api无法调用






path=sys.path[0]+r'/1.txt'
num1 = 0
num2 = 0
roundnum = 0
totalroundnum = 100

def gettoken(refresh_token):
    headers={'Content-Type':'application/x-www-form-urlencoded'
            }
    data={'grant_type': 'refresh_token',
          'refresh_token': refresh_token,
          'client_id':id,
          'client_secret':secret,
          'redirect_uri':'http://localhost:53682/'
         }
    html = req.post('https://login.microsoftonline.com/common/oauth2/v2.0/token',data=data,headers=headers)
    jsontxt = json.loads(html.text)
    refresh_token = jsontxt['refresh_token']
    access_token = jsontxt['access_token']
    with open(path, 'w+') as f:
        f.write(refresh_token)
    return access_token
def main():
    fo = open(path, "r+")
    refresh_token = fo.read()
    fo.close()
    global num1
    global num2
    global roundnum
    global totalroundnum
    global localtime
    num2 = 0
    localtime = time.asctime( time.localtime(time.time()) )
    access_token=gettoken(refresh_token)
    headers={
    'Authorization':access_token,
    'Content-Type':'application/json'
    }
    try:
        if req.get(r'https://graph.microsoft.com/v1.0/me/drive/root',headers=headers).status_code == 200:
            num1+=1
            num2+=1
            print('graph.microsoft.com/v1.0/me/drive/root - Success')
        else:
            print('graph.microsoft.com/v1.0/me/drive/root - Failure')
        if req.get(r'https://graph.microsoft.com/v1.0/me/drive',headers=headers).status_code == 200:
            num1+=1
            num2+=1
            print('graph.microsoft.com/v1.0/me/drive - Success')
        else:
            print('graph.microsoft.com/v1.0/me/drive - Failure')
        if req.get(r'https://graph.microsoft.com/v1.0/drive/root',headers=headers).status_code == 200:
            num1+=1
            num2+=1
            print('graph.microsoft.com/v1.0/drive/root - Success')
        else:
            print('graph.microsoft.com/v1.0/drive/root - Failure')
        if req.get(r'https://graph.microsoft.com/v1.0/users ',headers=headers).status_code == 200:
            num1+=1
            num2+=1
            print('graph.microsoft.com/v1.0/users - Success')
        else:
            print('graph.microsoft.com/v1.0/users - Failure')
        if req.get(r'https://graph.microsoft.com/v1.0/me/messages',headers=headers).status_code == 200:
            num1+=1
            num2+=1
            print('graph.microsoft.com/v1.0/me/messages - Success')  
        else:
            print('graph.microsoft.com/v1.0/me/messages - Failure')  
        if req.get(r'https://graph.microsoft.com/v1.0/me/mailFolders/inbox/messageRules',headers=headers).status_code == 200:
            num1+=1
            num2+=1
            print('graph.microsoft.com/v1.0/me/mailFolders/inbox/messageRules - Success')   
        else:
            print('graph.microsoft.com/v1.0/me/mailFolders/inbox/messageRules - Failure') 
        if req.get(r'https://graph.microsoft.com/v1.0/me/mailFolders/inbox',headers=headers).status_code == 200:
            num1+=1
            num2+=1
            print('graph.microsoft.com/v1.0/me/mailFolders/inbox - Success')
        else:
            print('graph.microsoft.com/v1.0/me/mailFolders/inbox - Failure')
        if req.get(r'https://graph.microsoft.com/v1.0/me/drive/root/children',headers=headers).status_code == 200:
            num1+=1
            num2+=1
            print('graph.microsoft.com/v1.0/me/drive/root/children - Success')
        else:
            print('graph.microsoft.com/v1.0/me/drive/root/children - Failure')
        if req.get(r'https://graph.microsoft.com/v1.0/me/mailFolders',headers=headers).status_code == 200:
            num1+=1
            num2+=1
            print('graph.microsoft.com/v1.0/me/mailFolders - Success')
        else:
            print('graph.microsoft.com/v1.0/me/mailFolders - Failure')
        if req.get(r'https://graph.microsoft.com/v1.0/me/outlook/masterCategories',headers=headers).status_code == 200:
            num1+=1
            num2+=1
            print('graph.microsoft.com/v1.0/me/outlook/masterCategories - Success')
        else:
            print('graph.microsoft.com/v1.0/me/outlook/masterCategories - Failure')
        if req.get(r'https://api.powerbi.com/v1.0/myorg/apps',headers=headers).status_code == 200:
            num1+=1
            num2+=1
            print('api.powerbi.com/v1.0/myorg/apps - Success') 
        else:
            print('api.powerbi.com/v1.0/myorg/apps - Failure')
    except:
        print(':( Something went wrong.')
        pass
for _ in range(totalroundnum):
    roundnum+=1
    print('\n================= START ( '+str(roundnum)+' / '+str(totalroundnum)+' ) =================')
    main()
    print('------ Summary ------')
    print('Success: '+str(num2))
    print('Total success: '+str(num1))
    print('Current time of server: ', localtime+'')
    print('================== END ( '+str(roundnum)+' / '+str(totalroundnum)+' ) ==================\n')
