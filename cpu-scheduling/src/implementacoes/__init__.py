"""
Os algoritmos de escalonamento a serem
implementados são os seguintes:
- First-Come, First-Served (FCFS)
- Shortest Job First (SJF)
- Round Robin (RR)
"""
class Escalonamento:
    def escalonamento_fcfs(self, processos):
        """
        Implementação do algoritimo de ordenação FCFS
        "Primeiro a Entrar, Primeiro a ser Atendido"
        O algoritmo FCFS é um algoritmo de escalonamento simples que agenda de acordo com os tempos de chegada dos processos.
        Os processos são executados na ordem em que chegam.

        Entrada: lista de dicionários dos processos no formato {"chegada": arrival, "burst": duration}
        Saída: média do tempo de retorno, média do tempo de resposta, média do tempo de espera
        """

        n = len(processos)
        tempo_de_espera = [0] * n
        tempo_de_retorno = [0] * n
        tempo_de_resposta = [0] * n

        # Ordena os processos por ordem de chegada, caso tenham o mesmo tempo de chegada, ordena por ordem de execução
        processos = sorted(processos, key=lambda x: x["chegada"])

        tempo_atual = 0
        
        for i in range(n):
            # Se o tempo atual for menor que o tempo de chegada do processo, atualiza o tempo atual
            if tempo_atual < processos[i]["chegada"]:
                tempo_atual = processos[i]["chegada"]
            
            # Calcular tempo de resposta, que é o tempo que o processo leva para começar a ser executado
            tempo_de_resposta[i] = tempo_atual - processos[i]["chegada"]
            tempo_de_espera[i] = tempo_de_resposta[i]
            
            # Atualiza o tempo atual
            tempo_atual += processos[i]["burst"]
            
            # Calcular tempo de retorno, que é o tempo que o processo leva para ser concluído
            tempo_de_retorno[i] = tempo_atual - processos[i]["chegada"]

        media_tempo_de_retorno = sum(tempo_de_retorno) / n
        media_tempo_de_resposta = sum(tempo_de_resposta) / n
        media_tempo_de_espera = sum(tempo_de_espera) / n

        return media_tempo_de_retorno, media_tempo_de_resposta, media_tempo_de_espera

    def escalonamento_sjf(self, processos):
        """
        Implementação do algoritimo de ordenação SJF (Menor Job Primeiro)
        O algoritmo SJF é um algoritmo de escalonamento que atribui o processo com o menor tempo de burst primeiro.

        Entrada: lista de dicionários dos processos no formato {"chegada": arrival, "burst": duration}
        Saída: média do tempo de retorno, média do tempo de resposta, média do tempo de espera
        """
        processos = sorted(processos, key=lambda x: x["chegada"])  # Ordena os processos por ordem de chegada
        n = len(processos)
        tempo_de_espera = [0] * n
        tempo_de_retorno = [0] * n
        tempo_de_resposta = [0] * n
        
        time = 0
        fila_de_espera = []
        feitos = 0
        
        while feitos < n:
            # Adciona os processos que chegaram até o tempo atual na fila de espera
            while processos and processos[0]["chegada"] <= time:
                fila_de_espera.append(processos.pop(0))
            
            if fila_de_espera:
                # Ordena a fila de espera pelo burst time
                fila_de_espera.sort(key=lambda x: x["burst"])
                
                # Process the shortest job
                current_process = fila_de_espera.pop(0)
                index = n - len(processos) - len(fila_de_espera) - 1
                
                if tempo_de_resposta[index] == 0:
                    tempo_de_resposta[index] = time - current_process["chegada"]
                
                time += current_process["burst"]
                tempo_de_retorno[index] = time - current_process["chegada"]
                tempo_de_espera[index] = tempo_de_retorno[index] - current_process["burst"]
                
                feitos += 1
            else:
                # Se a fila de espera estiver vazia, avança o tempo até o próximo processo chegar
                time = processos[0]["chegada"]
        
        media_tempo_de_retorno = sum(tempo_de_retorno) / n
        media_tempo_de_resposta = sum(tempo_de_resposta) / n
        media_tempo_de_espera = sum(tempo_de_espera) / n
        
        return media_tempo_de_retorno, media_tempo_de_resposta, media_tempo_de_espera


    def escalonamento_rr(self, processos, time_quantum=2):
        """
        Implementação do algoritimo de ordenação RR (Round Robin)
        O algoritmo RR é um algoritmo de escalonamento que atribui um quantum de tempo para cada processo.

        Entrada: lista de dicionários dos processos no formato {"chegada": arrival, "burst": duration}
        Saída: média do tempo de retorno, média do tempo de resposta, média do tempo de espera
        """
        n = len(processos)
        tempo_restante = [p['burst'] for p in processos]
        tempo_de_completacao = [0] * n
        tempo_de_retorno = [0] * n
        tempo_de_espera = [0] * n
        tempo_de_resposta = [-1] * n
        
        time = 0
        fila = []
        i = 0
        
        while True:
            # Adiciona os processos que chegaram até o tempo atual na fila
            while i < n and processos[i]['chegada'] <= time:
                fila.append(i)
                i += 1
            # Se a fila estiver vazia, avança o tempo até o próximo processo chegar
            if not fila:
                if i >= n:
                    break
                time = processos[i]['chegada']
                continue
            
            current = fila.pop(0)
            # Calcula o tempo de resposta do processo
            if tempo_de_resposta[current] == -1:
                tempo_de_resposta[current] = time - processos[current]['chegada']
            
            # Processa o processo atual, se o tempo restante for menor que o quantum, processa o tempo restante
            if tempo_restante[current] <= time_quantum:
                time += tempo_restante[current]
                tempo_de_completacao[current] = time
                tempo_restante[current] = 0
            else:
                # Processa o quantum de tempo e adiciona o processo de volta à fila
                time += time_quantum
                tempo_restante[current] -= time_quantum
                
                # Adiciona os processos que chegaram até o tempo atual na fila
                while i < n and processos[i]['chegada'] <= time:
                    fila.append(i)
                    i += 1
                
                fila.append(current)
        
        # Calcula o tempo de retorno e de espera de cada processo
        for i in range(n):
            tempo_de_retorno[i] = tempo_de_completacao[i] - processos[i]['chegada']
            tempo_de_espera[i] = tempo_de_retorno[i] - processos[i]['burst']
        
        media_tempo_de_retorno = sum(tempo_de_retorno) / n
        media_tempo_de_resposta = sum(tempo_de_resposta) / n
        media_tempo_de_espera = sum(tempo_de_espera) / n
        
        return media_tempo_de_retorno, media_tempo_de_resposta, media_tempo_de_espera