

def read_from_file(path):
    with open(path, 'r') as file:
        return file.read()


if __name__ == '__main__':
    datapaths = {
        'a': 'data/a_example.txt',
        'b': 'data/b_lovely_landscapes.txt'
    }

    filepath = datapaths['b']

    content = read_from_file(filepath)
    splited_content = content.split(sep='\n')

    amount_of_pictures = int(content[0])
    print(amount_of_pictures)

    picture_collection = []
    for i, row in enumerate(splited_content[1:-1]):
        splitted_row = row.split(' ')
        direction, amount_of_tags, tags = splitted_row[0], splitted_row[1], splitted_row[2:]
        picture = {'id': i, 'direction': direction, 'number_of_tags': int(amount_of_tags), 'tags': set(tags)}
        picture_collection.append(picture)

    picture_collection.sort(key=lambda pic: pic['number_of_tags'], reverse=True)
    v_pic_collection = [pic for pic in picture_collection if pic['direction'] == 'V']
    h_pic_collection = [pic for pic in picture_collection if pic['direction'] == 'H']

    # merged_pic_collection = []
    # for pic in v_pic_collection:
    #     idx = pic['id']
    #     for inner_pic in v_pic_collection:
    #         temp_merged_v_collection = []
    #         if idx != inner_pic['id']:
    #             temp_merged_v_collection.append({
    #                 'id1': pic['id'],
    #                 'id2': inner_pic['id'],
    #                 'direction': pic['direction'],
    #                 'all_tags': pic['tags'].union(inner_pic['tags']),
    #                 'common': len(pic['tags'].intersection(inner_pic['tags']))
    #             })
    #
    #         temp_merged_v_collection.sort(key=lambda pic: pic['common'], reverse=True)

    best_slides = []
    for pic in picture_collection:
        idx = pic['id']
        temp_collection = []
        for inner_pic in picture_collection:
            if idx != inner_pic['id']:
                temp_collection.append({
                    'idx1': pic['id'],
                    'idx2': inner_pic['id'],
                    'direction': pic['direction'],
                    'common_amount': len(inner_pic['tags'].intersection(pic['tags'])),
                    'left_amount': len(pic['tags'].difference(inner_pic['tags'])),
                    'right_amount': len(inner_pic['tags'].difference(pic['tags']))
                })

        temp_collection.sort(
            key=lambda pics: min(pics['common_amount'], pics['left_amount'], pics['right_amount']),
            reverse=True)
        print(temp_collection[0])
        best_slides.append(temp_collection[0])

    slides = []
    for slide in best_slides:
        if (slide['idx1'] not in slides) and (slide['idx2'] not in slides):
            slides.append(slide['idx1'])
            slides.append(slide['idx2'])

    with open('data/b_output.txt', 'w+') as file:
        file.write(str(len(slides)) + '\n')
        for slide in slides:
            file.write(str(slide) + '\n')
