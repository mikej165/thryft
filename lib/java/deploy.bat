@ECHO OFF
CALL mvn clean package -Dmaven.test.skip=true deploy
git add mvn-repo
git commit -a -m "deploy"
git push
