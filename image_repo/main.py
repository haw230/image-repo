import click
import pandas as pd

from constants import REPONAME
from datetime import datetime

@click.group()
def image_repo():
    pass

@image_repo.command()
@click.argument('repo_name')
def create_repo(repo_name):
    if not repo_name:
        click.echo('Please provide a name for the repo')
    
    df = pd.DataFrame(columns=["image_bytes", "date_added"])
    df.to_csv(f'{REPONAME}/{repo_name}.csv', index=False)

@image_repo.command()
@click.argument('filepath')
@click.argument('repo_name')
def add_image(filepath, repo_name):
    if not filepath:
        click.echo('Please provide a filepath')
    with open(filepath, 'rb') as img:
        f = img.read()
        image_bytes = bytearray(f)
    
    cur_data = pd.read_csv(f'{REPONAME}/{repo_name}.csv').to_dict('records')
    cur_data.append({
        'image_bytes': bytes(image_bytes),
        'date_added': datetime.now()
    })
    pd.DataFrame(cur_data).to_csv(f'{REPONAME}/{repo_name}.csv', index=False)

@image_repo.command()
@click.argument('repo_name')
def list_images(repo_name):
    df = pd.read_csv(f'{REPONAME}/{repo_name}.csv')
    df.drop(columns=[''])
    click.echo(df)

@image_repo.command()
@click.argument('repo_name')
def dump_images(repo_name):
    df = pd.read_csv(f'{REPONAME}/{repo_name}.csv')
    for row in df.to_dict('records'):
        with open(f'image_dump/{repo_name}/{row["date_added"]}.png') as f:
            f.write(bytes(row['image_bytes']))
    click.echo('Dumped all images!')

if __name__ == '__main__':
    image_repo()
