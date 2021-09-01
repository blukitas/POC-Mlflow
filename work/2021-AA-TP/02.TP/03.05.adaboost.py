start = time.time()
kfold =StratifiedKFold(n_splits=12,random_state = 42)
from sklearn.ensemble import AdaBoostClassifier
scorer_fn = make_scorer(f1_score, average='weighted') # seteamos una metrica apropiada al problema multiclase
parameters = {"n_estimators": range(10, 3000, 5), "learning_rate": np.arange(0, 3, 0.001)}
clf = RandomizedSearchCV(
    AdaBoostClassifier(DecisionTreeClassifier(class_weight="balanced")), 
    parameters, 
    n_jobs=12, 
    scoring=scorer_fn, 
    cv=kfold, 
    n_iter=3000
)

clf.fit(X_train, y_train)
ab = clf.best_estimator_
print(clf.best_score_, clf.best_params_)
print("F1-score training : {:.3f}".format(ab.score(X_train, y_train)))
print("F1-score test: {:.3f}".format(ab.score(x_test, y_test)))

end = time.time()
print(f"Tiempo: { end - start }")

# results
'''
/usr/local/lib/python3.7/dist-packages/sklearn/model_selection/_split.py:296: FutureWarning: Setting a random_state has no effect since shuffle is False. This will raise an error in 0.24. You should leave random_state to its default (None), or set shuffle=True.
  FutureWarning
0.4816592906103962 {'n_estimators': 2730, 'learning_rate': 0.549}
Accuracy training : 1.000
Accuracy test: 0.504
Tiempo: 4753.056187391281
'''

'''
import pickle
now = datetime.datetime.now()
pickle.dump(ab, open('AdaBoost_2606_2056h.pkl', 'wb'))
clf_results = pd.DataFrame(clf.cv_results_)
#pd.DataFrame(clf.cv_results_).to_csv('AdaBoost_h.RandomizedSearchCV.{0}'.format(now.strftime("%Y-%m-%d"))
clf_results.to_csv('AdaBoost_2056h.RandomizedSearchCV.{0}'.format(now.strftime("%Y-%m-%d")))
clf_results
'''


# matriz de confusión y classification_report
y_pred_test = ab.predict(x_test)
confusion_matrix(y_test, y_pred_test)

# heat map
cm = confusion_matrix(y_test, y_pred_test)
sns.heatmap(cm, cmap="Blues", annot=True, fmt="g")
plt.xlabel("Predicted")
plt.ylabel("True")
