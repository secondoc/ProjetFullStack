db = db.getSiblingDB("wiki_db");
db.wiki_tb.drop()

db.wiki_tb.insertMany([
    {
        "id" : 1,
        "name" : "Wiki1",
    },
    {
        "id" : 2,
        "name" : "Wiki2",
    }
]);