PRAGMA synchronous = OFF;
PRAGMA journal_mode = MEMORY;
BEGIN TRANSACTION;
CREATE TABLE "cebarbie_barbiepage" (
  "id" int(11) NOT NULL ,
  "name" longtext NOT NULL,
  "image_path" longtext NOT NULL,
  "original_text" longtext NOT NULL,
  "width" int(11) NOT NULL,
  "height" int(11) NOT NULL,
  "text_x" int(11) NOT NULL,
  "text_y" int(11) NOT NULL,
  "text_w" int(11) NOT NULL,
  "text_h" int(11) NOT NULL,
  PRIMARY KEY ("id")
);
INSERT INTO "cebarbie_barbiepage" VALUES (1,'Barbie at Kitchen Table with Laptop','barbie-at-kitchen-table','"I''m only creating the design ideas," Barbie says, laughing. "I''ll need Steven''s and Brian''s help to turn it into a real game!"',600,518,5,430,590,90);
INSERT INTO "cebarbie_barbiepage" VALUES (2,'Barbie Holding Laptop In Class','barbie-holding-computer-in-class
','At computer class, Barbie presents the game she designed. Ms. Smith is so impressed that she gives Barbie extra credit! Barbie''s terrific computer skills have saved the day for both sisters! "I guess I can be a computer engineer!" says Barbie happily.',599,580,0,425,595,156);
INSERT INTO "cebarbie_barbiepage" VALUES (3,'Skipper and Barbie hug with laptop','skipper-barbie-hug-with-laptop','The next morning, Barbie gives her sister a big surprise. Skipper turns on her laptop--and it works! "My lost assignment!" cries Skipper. "You are just too cool, Barbie! you fixed my computer and saved my homework!" Skipper gives Barbie a big hug.',450,480,50,6,355,95);
INSERT INTO "cebarbie_barbiepage" VALUES (4,'Barbie hunched over computer','barbie-hunched-at-computer','After class, Barbie meets with Steven and Brian in the library. "Hi, guys," says Barbie. I tried to send you my designs, but I ended up crashing my laptop--and Skipper''s, too! I need to get back the lost files and repair both of our laptops.',557,549,70,12,420,100);
INSERT INTO "cebarbie_barbiepage" VALUES (5,'Barbie with CD and guys','barbie-with-cd-and-guys','"It will go faster if Brian and I help," offers Steven. "Great!" says Barbie. "Steven, can you hook Skipper''s hard drive up to the library''s computer?" "Sure!" says Steven. "The library computer has excellent security software to protect it."',600,630,125,8,450,115);
INSERT INTO "cebarbie_barbiepage" VALUES (6,'Barbie hacking in kitchen with Skipper','barbie-hacking-in-kitchen-with-skipper2','Barbie tries to email her design to Steven, but suddenly her screen starts blinking. "That''s weird!" says Barbie. Barbie and Skipper try to reboot the computer but nothing happens. "Looks like you''ve got a virus, big sister," says Skipper.',600,589,2,440,595,160);
INSERT INTO "cebarbie_barbiepage" VALUES (7,'Skipper Looking At Barbie''s Concept Art','skipper-looking-at-dog-drawing','"Your robot puppy is so sweet," says Skipper. "Can I play your game?" "I''m only creating the design ideas," Barbie says, laughing, "I''ll need Steven''s and Brian''s help to turn it into a real game!"',600,641,75,5,416,100);
INSERT INTO "cebarbie_barbiepage" VALUES (8,'Barbie Skipper Computer Anguish','barbie-skipper-computer-anguish','When Barbie puts her flash drive into Skipper''s laptop, the screen starts blinking. "Oh no!" says Barbie. "The virus must be on the flash drive!" "I forgot to back up my homework assignment!" cries Skipper. "And all my music files are lost, too!"',600,600,12,420,590,177);
INSERT INTO "cebarbie_barbiepage" VALUES (9,'Barbie Skipper Pillowfight','barbie-skipper-pillowfight','"I''m so sorry, Skipper," says Barbie. "I have to run off to school now. But I promise to find a way to fix your laptop." "You better!" Skipper replies as she playfully hits Barbie with a pillow.',515,560,31,7,315,90);
INSERT INTO "cebarbie_barbiepage" VALUES (10,'Barbie In Class','barbie-in-class-taking-notes','Barbie makes it to computer class just before the bell rings. As soon as class begins, Barbie raises her hand. "Yes, Barbie?" asks Ms. Smith, the teacher. "If your computer gets a virus and crashes, how can you retrieve all the files you lost?" asks Barbie.',600,640,75,20,405,119);
INSERT INTO "cebarbie_barbiepage" VALUES (11,'High Five','barbie-guy-highfive','"I''ve got Skipper''s assignment from the hard drive!" exclaims Steven. "Fantastic!" says Barbie. "And her other files, as well?" "I''ve got everything," says Steven.  "Now let''s retrieve the files from your hard drive. Both laptops will be as good as new in no time!"',450,480,59,13,362,67);
END TRANSACTION;
