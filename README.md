# Shipping Database

source: https://www.equasis.org/

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
# playwright codegen https://www.equasis.org/
```

## 4. Execute streamlit

```
# streamlit run app/dashboard.py
```

access to http://127.0.0.1:8501


# 5. Execute Robot

```
# python3 robot.py scrape 9226396
```

8300614
9226396

# 6. make exe files for Windows

- requirement
  - python3 and virtualenv

- Edit app.spec

 $ cp app.spec.linux app.spec
 $ cp app.spec.windows10 app.spec
 $ cp app.spec.windows11 app.spec

- Run Command

 $ pyinstaller app.spec --clean

# Reference

https://github.com/excelle08/py-equasis-crawler/blob/1db4470a4c832dd2bdcef4803b8cea927cbee32f/equasis-idonly.py#L120
https://medium.com/@pepitotakanorioor/howto-scraper-in-python-playwright-fastapi-and-aws-lambda-container-8f9235155471

https://medium.com/@pepitotakanorioor/howto-scraper-in-python-playwright-fastapi-and-aws-lambda-container-8f9235155471

https://zenn.dev/shimakaze_soft/articles/4c0784d9a87751
https://alembic.sqlalchemy.org/en/latest/autogenerate.html


ETL::Pipelineはこれがわかりやすい

https://metacpan.org/pod/ETL::Pipeline

https://medium.com/@dheerajbesu/create-streamlit-as-desktop-app-54bb843974f3
https://stackoverflow.com/questions/69058232/how-can-i-create-onedir-file-from-spec-file-using-pyinstaller

https://medium.com/@jyotikhetan2/creating-a-pdf-viewer-with-streamlit-uploading-and-displaying-pdf-files-26587097d047
