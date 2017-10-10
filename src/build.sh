# VAR_A=yohohoho
# VAR_B=muahahah
sed \
-e "s/\${VAR_A}/'${VAR_A}'/" \
-e "s/\${VAR_B}/'${VAR_B}'/" \
config/env_build.cfg > config/env.cfg