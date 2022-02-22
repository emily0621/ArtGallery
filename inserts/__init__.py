from inserts.viewer_insert import viewerInsert
from inserts.author_insert import authorInsert
from inserts.category_insert import categoryInsert
from inserts.post_insert import postInsert


def runInserts():
    viewerInsert()
    authorInsert()
    categoryInsert()
    postInsert()


if __name__ == "__main__":
    runInserts()
