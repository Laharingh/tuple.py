{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "86ec2c7c-b386-4562-813f-af4980c4c4a7",
   "metadata": {},
   "outputs": [
    {
     "ename": "AttributeError",
     "evalue": "'set' object has no attribute 'discards'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mAttributeError\u001b[39m                            Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[1]\u001b[39m\u001b[32m, line 2\u001b[39m\n\u001b[32m      1\u001b[39m eids={\u001b[32m101\u001b[39m,\u001b[32m102\u001b[39m,\u001b[32m103\u001b[39m,\u001b[32m104\u001b[39m,\u001b[32m105\u001b[39m,\u001b[32m106\u001b[39m,\u001b[32m107\u001b[39m,\u001b[32m108\u001b[39m}\n\u001b[32m----> \u001b[39m\u001b[32m2\u001b[39m \u001b[43meids\u001b[49m\u001b[43m.\u001b[49m\u001b[43mdiscards\u001b[49m(\u001b[32m102\u001b[39m)\n\u001b[32m      3\u001b[39m \u001b[38;5;28mprint\u001b[39m(eids)\n\u001b[32m      4\u001b[39m eids.discard(\u001b[32m109\u001b[39m)\n",
      "\u001b[31mAttributeError\u001b[39m: 'set' object has no attribute 'discards'"
     ]
    }
   ],
   "source": [
    "eids={101,102,103,104,105,106,107,108}\n",
    "eids.discards(102)\n",
    "print(eids)\n",
    "eids.discard(109)\n",
    "print(eids)\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "be0e90b1-88c6-4ff6-9e14-88d9736503b1",
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.11.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
