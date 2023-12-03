# Development

## 1. Lauching Docker container and login

```
$ docker compose build
$ docker compose up -d
$ docker exec -it shipping-app bash
```

```
$ xhost +
```

## 2. Database setup

```
alembic upgrade head
```

If some revisions exist, run the command followed

```
alembic revision --autogenerate -m "Some comment"
```


## 3. Setting playwright test

```
# playwright codegen https://xxxxx.org/
```

## 4. Execute streamlit

```
# streamlit run dashboard.py
```

access to http://127.0.0.1:8501


# 5. Execute Robot

```
# python3 robot.py scrape
```

# 6. make exe files for Windows

- requirement
  - python3 and virtualenv

- Edit app.spec

 $ cp app.spec.linux app.spec
 $ cp app.spec.windows11 app.spec

- Run Command

 $ pyinstaller app.spec --clean
