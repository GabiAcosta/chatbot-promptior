Para empezar me gustaría decir que este fue un proyecto muy desafiante e interesante a la vez, ya que en su gran mayoría fue todo nuevo para mi, no conocía la tecnología de Langchain ni había trabajado con IA antes, por lo tanto fue todo un reto aprender cómo funciona el desarrollo RAG y los elementos que lo conforman como puede ser Langchain, los LLM o las BD vectoriales como Pinecone o FAISS.

Dicho eso, el primer desafío fue aprender sobre Langchain y cómo llevar a cabo un chatbot, lo cual pude ir aprendiendo leyendo la documentación y guiándome con varias guías/tutoriales por internet. 

El desarrollo del chatbot al inicio se me hizo difícil ya que no estaba consultando la información que yo le pasaba via URL pero luego de seguir leyendo la documentación me encontré con unos templates que facilita Langchain para la creación de varios casos de usos de LLM, en este caso, un chatbot.

El siguiente desafío fue nutrir al LLM con la información requerida, ahí es donde entra en juego Pinecone y su BD vectorial, en donde subí en forma de PDF la información que se encuentra en la página web de Promptior que posteriormente iba a ser indexada en la BD.

Una vez todo conectado, el chatbot ya era capaz de responder las preguntas sobre Promptior con gran precisión, por lo tanto solo quedaba el deploy que fue mi mayor desafío.

Para el deploy también tuve que informarme bastante via documentación y tutoriales ya que era un apartado que no había tocado directamente con anterioridad. Al inicio opté por Azure pero luego de varios intentos opté por utilizar Railway como se aconsejaba en la letra. Con Railway también tuve complicaciones debido a problemas con dependencias y librerías de Python pero luego de varios intentos y aprender a usar Poetry para configurar las dependencias, tuve éxito y pude llevar a cabo el deploy.
