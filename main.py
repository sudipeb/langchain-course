from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_ollama import ChatOllama 

def _sanitize_ssl_environment():
    ssl_cert_file = os.environ.get("SSL_CERT_FILE")
    if ssl_cert_file and not os.path.exists(ssl_cert_file):
        os.environ.pop("SSL_CERT_FILE", None)


load_dotenv()


def main():
    _sanitize_ssl_environment()

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=1.0,  # Gemini 3.0+ defaults to 1.0
        max_tokens=None,
        timeout=None,
        max_retries=2,
    )
    # llm=ChatOllama(temperature=0,model="gemma3:270m")
    print("Hello from langchain-course!")
    information = '''Vladimir Vladimirovich Putin[h] (born 7 October 1952) is a Russian politician and former intelligence officer who has served as President of Russia since 2012, having previously served from 2000 to 2008. Putin also served as Prime Minister of Russia from 1999 to 2000[i] and again from 2008 to 2012. He has been described as the de facto leader of Russia since 2000.

Born in Leningrad (now Saint Petersburg), Putin worked as a KGB foreign intelligence officer for 16 years, rising to the rank of lieutenant colonel. He resigned in 1991 to begin a political career in Saint Petersburg. In 1996, Putin moved to Moscow to join the administration of President Boris Yeltsin. He briefly served as the director of the Federal Security Service (FSB) and then as secretary of the Security Council of Russia before being appointed prime minister in August 1999. Following Yeltsin's resignation, Putin became acting president and, less than three months later in March 2000, was elected to his first term as president. He was reelected in 2004. Due to constitutional limitations on two consecutive presidential terms, Putin served as prime minister again from 2008 to 2012 under Dmitry Medvedev. He returned to the presidency in 2012, following an election marked by allegations of fraud and protests, and was reelected in 2018.

During Putin's initial presidential tenure, the Russian economy grew on average by seven percent per year as a result of economic reforms and a fivefold increase in the price of oil and gas.[11][12] Additionally, Putin led Russia in a conflict against Chechen separatists, re-establishing federal control over the region.While serving as prime minister under Medvedev, he oversaw the Russo-Georgian War, alongside enacting military and police reforms. In his third presidential term, Russia occupied and annexed Crimea as well as supported a war in eastern Ukraine through several military incursions, resulting in international sanctions, which, together with a drop in oil prices on the international markets, led to the financial crisis in Russia.[15] Additionally, he ordered a military intervention in Syria to support his ally, President Bashar al-Assad, during the Syrian civil war. In April 2021, after a referendum, he signed constitutional amendments into law that included one allowing him to run for reelection twice more, potentially extending his presidency to 2036.[16][17] In February 2022, during his fourth presidential term, Putin launched a full-scale invasion of Ukraine, which prompted international condemnation and led to expanded sanctions. In September 2022, he announced a partial mobilization and forcibly annexed four Ukrainian oblasts into Russia. In March 2023, the International Criminal Court issued an arrest warrant for Putin for war crimes[18] related to his alleged criminal responsibility for illegal child abductions during the war.[19] In March 2024, he was reelected to another term.

Under Putin's rule, the Russian political system has been transformed into an authoritarian dictatorship with a personality cult. His rule has been marked by endemic corruption and widespread human rights violations, including the imprisonment and suppression of political opponents, intimidation and censorship of independent media in Russia, and a lack of free and fair elections.Russia has consistently received very low scores on Transparency International's Corruption Perceptions Index, The Economist Democracy Index, Freedom House's Freedom in the World index, and the Reporters Without Borders' World Press Freedom Index.'''
    summary_template='''Given the information{information}about  a person I want you to create:
    1. A short summary
    2. two interesting facts'''
    summary_prompt_template=PromptTemplate(input_variables=["information"],template=summary_template)
    chain=summary_prompt_template|llm
    response=chain.invoke(input={'information':information})
    print(response.content)


if __name__ == "__main__":
    main()
