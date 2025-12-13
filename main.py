{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "2def3d9f",
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "FastAPI.get() missing 1 required positional argument: 'path'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[0;32mIn [15], line 9\u001b[0m\n\u001b[1;32m      3\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mpandas\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m \u001b[38;5;21;01mpd\u001b[39;00m\n\u001b[1;32m      6\u001b[0m app \u001b[38;5;241m=\u001b[39m FastAPI\n\u001b[0;32m----> 9\u001b[0m \u001b[38;5;129m@app\u001b[39m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mget\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[38;5;124;43m/hello\u001b[39;49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[43m)\u001b[49m\n\u001b[1;32m     10\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21mread_root\u001b[39m():\n\u001b[1;32m     11\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m {\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mHello\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mWorld\u001b[39m\u001b[38;5;124m\"\u001b[39m}\n\u001b[1;32m     14\u001b[0m \u001b[38;5;129m@app\u001b[39m\u001b[38;5;241m.\u001b[39mget(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m/\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[1;32m     15\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21mroot\u001b[39m():\n",
      "\u001b[0;31mTypeError\u001b[0m: FastAPI.get() missing 1 required positional argument: 'path'"
     ]
    }
   ],
   "source": [
    "from fastapi import FastAPI, Path\n",
    "from pydantic import BaseModel\n",
    "import pandas as pd\n",
    "\n",
    "\n",
    "app = FastAPI\n",
    "\n",
    "\n",
    "@app.get(\"/hello\")\n",
    "def read_root():\n",
    "    return {\"Hello\": \"World\"}\n",
    "\n",
    "\n",
    "@app.get(\"/\")\n",
    "def root():\n",
    "    return {'Hello World': 'Welcome to our devops learning'}\n",
    "    \n",
    "@app.get('/all_servers')\n",
    "def get_servers():\n",
    "    x = pd.read_excel('servers.xlsx')\n",
    "    return x\n",
    "\n",
    "@app.get('/server')\n",
    "def get_servers(server_ip):\n",
    "    x = pd.read_excel('servers.xlsx')\n",
    "    return x[x['ip']==server_ip]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "58d48eff",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (4045261450.py, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  Cell \u001b[0;32mIn [1], line 1\u001b[0;36m\u001b[0m\n\u001b[0;31m    pip install fastapi, uvicorn\u001b[0m\n\u001b[0m        ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "pip install fastapi, uvicorn\n",
    "uvicorn main:app --reload #start app\n",
    "localhost/doc  #swaggerui\n",
    "localhost/redocdoc  #redoc style"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "2ad30ca1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'item'"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def get(item: int):\n",
    "    return item\n",
    "\n",
    "get('item')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "74a197a8",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fb5dbdce",
   "metadata": {},
   "outputs": [],
   "source": [
    "#"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
