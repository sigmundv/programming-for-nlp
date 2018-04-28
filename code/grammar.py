import nltk

fs1 = nltk.FeatStruct(gender='f', person=3, number='sg')

fs2 = nltk.FeatStruct(
    word="íbúð",
    pos='n',
    definiteness="def-",
    middle="na",
    agreement=fs1,
    case='nom',
    nounType='count',
    verbType='na',
    tense='na',
    ls='na')

print(fs2)
