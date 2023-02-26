pipeline {
    agent{any{}}
  stages {
         stage('Get Code') {
            steps {
                 git 'https://github.com/an-mengqi/selenium-autotests.git'
            }
         }
    stage('build') {
      steps {
        sh 'pip install --user -r requirements.txt'
      }
    }
    stage('test') {
      steps {
        sh 'pytest tests/test_admin.py --url=http://192.168.0.15:8081/admin'
      }
    }
  }
}
