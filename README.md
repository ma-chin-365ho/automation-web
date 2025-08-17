# automation-web

# command
## install
```
pip install -r requirements.txt
```

## .env
```
URL_MY_YMOBILE_LOGIN='https://xxx'
ID_MY_YMOBILE='xxx'
PW_MY_YMOBILE='xxx'
PIN_MY_YMOBILE='xxx'
URL_MY_SOFTBANK_BB_LOGIN='https://xxx'
ID_MY_SOFTBANK_BB='xxx'
PW_MY_SOFTBANK_BB='xxx'
```

## exec
```
python automation_softbank_bb.py
python automation_ymobile.py
```

## check log
```
playwright show-trace log/trace.zip --host 0.0.0.0
```