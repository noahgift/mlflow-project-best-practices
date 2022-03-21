import pandas as pd
import mlflow
import click
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

def human_readable(value):
    if value == ['1']:
        return "FAKE NEWS!"
    return "REAL NEWS"

def predict(text):
    print(f"Accepted payload: {text}")
    my_data = {
        "text": {0: text},
    }
    data = pd.DataFrame(data=my_data)
    # Load model as a PyFuncModel.
    loaded_model = mlflow.pyfunc.load_model('model')
    result = loaded_model.predict(pd.DataFrame(data))
    return human_readable(result)


@click.command()
@click.option(
    "--text",
    help="Pass in text for real or fake news",
)
def predictcli(text):
    """Predict news real or fake"""

    result = predict(text)
    if "FAKE" in result:
        click.echo(click.style(result, bg="red", fg="white"))
    else:
        click.echo(click.style(result, bg="red", fg="white"))

if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    predictcli()
