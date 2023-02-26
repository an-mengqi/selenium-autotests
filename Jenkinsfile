pipeline {
    agent{
        args '-e "HOME=/Users/anastasiiamonakhova/.jenkins/workspace/homework"'
        docker{ image 'python:3' }
    }
  stages {
         stage('Get Code') {
            steps {
                 sh 'rm -r *'
                 sh 'git clone https://github.com/an-mengqi/selenium-autotests.git'
            }
         }
    stage('build') {
      steps {
        sh 'pip install --user -r selenium-autotests/requirements.txt'
      }
    }
    stage('test') {
      steps {
        sh 'pytest selenium-autotests/tests/test_admin.py --url=http://192.168.0.15:8081/admin'
      }
    }
  }
}
