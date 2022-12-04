#Create your empty list of AWS services
aws_serviceslist= []

#Populate your list oAWS Serviceslist
aws_serviceslist.append('AWS Codecommit')
aws_serviceslist.append('AWS Codebuild')
aws_serviceslist.append('AWS Codedeploy')
aws_serviceslist.append('AWS CloudHSM')
aws_serviceslist.append('AWS Shield')
aws_serviceslist.append('Amazon Cognito')
aws_serviceslist.append('Amazon ElastiCache')
aws_serviceslist.append('AWS Security Hub')
aws_serviceslist.append('AWS Beanstalk')
aws_serviceslist.append('Amazon EventBridge')

#Print the list oAWS Serviceslist and its length
print("10 Must include AWS and Azon Serviceslist")
print(len(aws_serviceslist))

#Remove two specifiAWS Serviceslist from the list by name or by index
del aws_serviceslist[0]
del aws_serviceslist[-1]

#Print the new list and its new length
print(aws_serviceslist)
print("8 Must include AWS and Azon Serviceslist")
print(len(aws_serviceslist))

