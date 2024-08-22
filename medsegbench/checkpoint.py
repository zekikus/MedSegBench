import torch

class BestModelCheckPoint:

    def __init__(self, model_name):
        self.best_score = 0
        self.model_name = model_name
    
    def check(self, score, model, seed, data_flag):
        if score > self.best_score:
            print("Best Score:", score)
            self.best_score = score
            torch.save(model.state_dict(), f"results/{data_flag}/{self.model_name}/model_{self.model_name}_seed_{seed}.pt")