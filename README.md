# Demona server check

client - vuejs client
src - python backend
lambdalayers - contains packed libraries for python

Creation of layer:
https://stackoverflow.com/questions/56959987/how-to-deploy-matplotlib-the-python-library-as-a-lambda-layer-in-aws
(Warning: do not remove numpy)

Advantage of layer:
1. Lambda can be small
2. Libraries can be compiled exactly for aws linux