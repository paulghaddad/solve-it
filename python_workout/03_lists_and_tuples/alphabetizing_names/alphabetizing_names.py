from operator import itemgetter


people = [{'first':'Reuven', 'last':'Lerner', 'email':'reuven@lerner.co.il'},
         {'first':'Donald', 'last':'Trump', 'email':'president@whitehouse.gov'},
          {'first':'Vladimir', 'last':'Putin', 'email':'president@kremvax.ru'}]


def alphabetizing_names(people):
    sorted_people = sorted(people, key=itemgetter('last', 'first'))
    return sorted_people

print(alphabetizing_names(people))
