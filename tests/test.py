from image_repo.main import create_repo, add_image, list_images, dump_images

create_repo('test')
add_image('download.jpg')
list_images()
dump_images('test')