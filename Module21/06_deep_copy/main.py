site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iphone',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}

def change(site, count, site_list):
    if count == 0:
        return site_list
    name = input('Введите название продукта для нового сайта:')
    site['html']['head']['title'] = 'Куплю/продам {name} недорого'.format(name=name)
    site['html']['body']['h2'] = 'У нас самая низкая цена на {name}'.format(name=name)
    site_list.append(site)
    print(site_list)
    change(site.copy(), count - 1, site_list)

count = 2#int(input('Сколько сайтов: '))
site_list = []
change(site.copy(), count, site_list)
