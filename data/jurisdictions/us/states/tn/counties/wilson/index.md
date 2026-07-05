---
type: Jurisdiction
title: "Wilson County, TN"
classification: county
fips: "47189"
state: "TN"
demographics:
  population: 158805
  population_under_18: 37178
  population_18_64: 96377
  population_65_plus: 25250
  median_household_income: 95839
  poverty_rate: 7.97
  homeownership_rate: 77.02
  unemployment_rate: 3.23
  median_home_value: 428000
  gini_index: 0.4372
  vacancy_rate: 6.17
  race_white: 128404
  race_black: 11470
  race_asian: 3618
  race_native: 426
  hispanic: 10359
  bachelors_plus: 55431
districts:
  - to: "us/states/tn/districts/05"
    rel: in-district
    area_weight: 0.5021
  - to: "us/states/tn/districts/06"
    rel: in-district
    area_weight: 0.4964
  - to: "us/states/tn/districts/senate/17"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/tn/districts/house/46"
    rel: in-district
    area_weight: 0.7391
  - to: "us/states/tn/districts/house/57"
    rel: in-district
    area_weight: 0.1965
  - to: "us/states/tn/districts/house/40"
    rel: in-district
    area_weight: 0.0642
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tn]
timestamp: "2026-07-03"
---

# Wilson County, TN

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 158805 |
| Under 18 | 37178 |
| 18–64 | 96377 |
| 65+ | 25250 |
| Median household income | 95839 |
| Poverty rate | 7.97 |
| Homeownership rate | 77.02 |
| Unemployment rate | 3.23 |
| Median home value | 428000 |
| Gini index | 0.4372 |
| Vacancy rate | 6.17 |
| White | 128404 |
| Black | 11470 |
| Asian | 3618 |
| Native | 426 |
| Hispanic/Latino | 10359 |
| Bachelor's or higher | 55431 |

## Districts

- [TN-05](/us/states/tn/districts/05.md) — 50% (congressional)
- [TN-06](/us/states/tn/districts/06.md) — 50% (congressional)
- [TN Senate District 17](/us/states/tn/districts/senate/17.md) — 100% (state senate)
- [TN House District 46](/us/states/tn/districts/house/46.md) — 74% (state house)
- [TN House District 57](/us/states/tn/districts/house/57.md) — 20% (state house)
- [TN House District 40](/us/states/tn/districts/house/40.md) — 6% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
