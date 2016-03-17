'''
Created on Feb 25, 2016

@author: michael.f.koegel
'''
"""
Working with media.py
"""
import Media #need to figure out why this won't reference my 'media.py file)
import fresh_tomatoes #need to figure out why this won't reference the 'fresh_tomatoes.py' file

#The section below is fairly generic. It's just my list of random movie to display on a web page.
toy_story = Media.Movie("Toy Story",
                        "81",
                        "Woody (Tom Hanks), a good-hearted cowboy doll who belongs to a young boy named Andy (John Morris), \
                        sees his position as Andy's favorite toy jeopardized when his parents buy him a Buzz Lightyear (Tim Allen)\
                         action figure. Even worse, the arrogant Buzz thinks he's a real spaceman on a mission to return to his home planet.\
                          When Andy's family moves to a new house, Woody and Buzz must escape the clutches of maladjusted\
                           neighbor Sid Phillips (Erik von Detten) and reunite with their boy.",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://youtu.be/KYz2wyBy3kc")
#print (toy_story.storyline)

avatar = Media.Movie("Avatar",
                     "162",
                     "On the lush alien world of Pandora live the Na'vi, beings who appear primitive but are highly evolved.\
                      Because the planet's environment is poisonous, human/Na'vi hybrids, called Avatars, must link to human\
                       minds to allow for free movement on Pandora. Jake Sully (Sam Worthington), a paralyzed former Marine,\
                        becomes mobile again through one such Avatar and falls in love with a Na'vi woman (Zoe Saldana).\
                         As a bond with her grows, he is drawn into a battle for the survival of her world.",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://youtu.be/5PSNL1qE6VY")
#print(avatar.storyline)
#avatar.show_trailer()

die_hard = Media.Movie("Die Hard",
                       "131",
                     "New York City policeman John McClane (Bruce Willis) is visiting his estranged wife (Bonnie Bedelia) and\
                      two daughters on Christmas Eve. He joins her at a holiday party in the headquarters of the Japanese-owned\
                       business she works for. But the festivities are interrupted by a group of terrorists who take over the\
                        exclusive high-rise, and everyone in it. Very soon McClane realizes that there's no one to save the hostages -- but him.",
                     "https://upload.wikimedia.org/wikipedia/en/7/7e/Die_hard.jpg",
                     "https://youtu.be/2TQ-pOvI6Xo")

deadpool = Media.Movie("Deadpool",
                       "108",
                     "Wade Wilson (Ryan Reynolds) is a former Special Forces operative who now works as a mercenary. His world\
                      comes crashing down when evil scientist Ajax (Ed Skrein) tortures, disfigures and transforms him into Deadpool.\
                       The rogue experiment leaves Deadpool with accelerated healing powers and a twisted sense of humor. With help\
                        from mutant allies Colossus and Negasonic Teenage Warhead (Brianna Hildebrand), Deadpool uses his new skills\
                         to hunt down the man who nearly destroyed his life.",
                     "https://upload.wikimedia.org/wikipedia/en/4/46/Deadpool_poster.jpg",
                     "https://youtu.be/ZIM1HydF9UA")

resident_evil = Media.Movie("Resident Evil",
                            "100",
                     "Based on the popular video game, Milla Jovovich and Michelle Rodriguez star as the leaders of a commando\
                      team who must break into 'the hive', a vast underground genetics laboratory operated by the powerful Umbrella\
                       Corporation. There, a deadly virus has been unleashed, killing the lab's personnel and resurrecting them as\
                        the evil Un-dead. The team has just three hours to shut down the lab's supercomputer and close the facility\
                         before the virus threatens to overrun the Earth.",
                     "https://upload.wikimedia.org/wikipedia/en/a/a1/Resident_evil_ver4.jpg",
                     "https://youtu.be/PWUT4CXWcwQ")

star_trek = Media.Movie("Star Trek",
                        "127",
                     "Aboard the USS Enterprise, the most-sophisticated starship ever built, a novice crew embarks on its maiden voyage.\
                      Their path takes them on a collision course with Nero (Eric Bana), a Romulan commander whose mission of\
                       vengeance threatens all mankind. If humanity would survive, a rebellious young officer named James T. Kirk (Chris Pine)\
                        and a coolly logical Vulcan named Spock (Zachary Quinto) must move beyond their rivalry and find a way\
                         to defeat Nero before it is too late.",
                     "https://upload.wikimedia.org/wikipedia/en/2/29/Startrekposter.jpg",
                     "https://youtu.be/iGAHnZ555nI")

#defining my list of movies that can change depending on what I want to display
movies = [toy_story, avatar, die_hard, deadpool, resident_evil, star_trek]

#passing the movies to the 'fresh tomatoes class to build the web page
fresh_tomatoes.open_movies_page(movies)

#print(media.Movie.VALID_RATINGS)