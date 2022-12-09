import jenkins
import json
#jenkins地址
jenkins_server_url='http://192.168.75.241:8086/jenkins'
#jenkins用户名
user_name='sky_jianghuakun'
#jenkins api token
api_token='11f2604ee249115b764d28f3d9d3943672'
#登录jenkins
server=jenkins.Jenkins(jenkins_server_url,user_name,api_token)
#获取jenkins版本
version=server.get_version()
#print(version)
#获取最后构建构建number
job_name='shc'
jenkins_buildID=server.get_job_info(job_name)['lastBuild']['number']
#print("1111",jenkins_buildID)
#获取下次构建number
next_build_number=server.get_job_info(job_name)['nextBuildNumber']
#print("2222",next_build_number)
#参数化构建
arg_dic = {"TestGroup": "test","mybranch": "v2.1.7","packegetype": "jar"}
#String参数化构建job名为job_name的job, 参数param_dict为字典形式，如：param_dict= {"param1"：“value1”， “param2”：“value2”}
#server.build_job(job_name, parameters=arg_dic)
#获取job名为job_name的job的相关信息
jenkins_info = server.get_job_info(job_name)
#print(jenkins_info,"######job_name的job的相关信息")
#获取工程配置
#print(server.get_job_config(job_name))
#获取工程数量
print(server.jobs_count())
#获取所有jobs
print(server.get_all_jobs())
#获取工程最后一次构建url
print(server.get_job_info(job_name)['lastBuild']['url'])
#获取工程构建控制台日志
print(server.get_build_console_output(job_name,jenkins_buildID))
#获取工程构建结果
print(server.get_build_info(job_name,jenkins_buildID)['result'])
#判断工程是否在构建中
print(server.get_build_info(job_name,jenkins_buildID)['building'])

