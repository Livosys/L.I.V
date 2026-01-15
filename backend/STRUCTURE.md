CORE FILES (DO NOT TOUCH)
- main.py
- feature_loader.py
- start_check.py
- main_check.py
- DEPLOY_GUARD.sh
- _create_feature.sh

FOLDERS
- routers/
- auth/
- observability/
- feature_x/ (and future features)

RULES
- ONLY cat << 'EOF'
- ALWAYS run DEPLOY_GUARD.sh before restart
- NEVER edit systemd overrides
