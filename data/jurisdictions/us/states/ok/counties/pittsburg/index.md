---
type: Jurisdiction
title: "Pittsburg County, OK"
classification: county
fips: "40121"
state: "OK"
demographics:
  population: 43561
  population_under_18: 9889
  population_18_64: 24897
  population_65_plus: 8775
  median_household_income: 55310
  poverty_rate: 17.74
  homeownership_rate: 71.44
  unemployment_rate: 5.74
  median_home_value: 156900
  gini_index: 0.4599
  vacancy_rate: 19.78
  race_white: 30277
  race_black: 1075
  race_asian: 215
  race_native: 3569
  hispanic: 2495
  bachelors_plus: 8267
districts:
  - to: "us/states/ok/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ok/districts/senate/7"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ok/districts/house/17"
    rel: in-district
    area_weight: 0.6157
  - to: "us/states/ok/districts/house/18"
    rel: in-district
    area_weight: 0.3542
  - to: "us/states/ok/districts/house/15"
    rel: in-district
    area_weight: 0.03
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ok]
timestamp: "2026-07-03"
---

# Pittsburg County, OK

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 43561 |
| Under 18 | 9889 |
| 18–64 | 24897 |
| 65+ | 8775 |
| Median household income | 55310 |
| Poverty rate | 17.74 |
| Homeownership rate | 71.44 |
| Unemployment rate | 5.74 |
| Median home value | 156900 |
| Gini index | 0.4599 |
| Vacancy rate | 19.78 |
| White | 30277 |
| Black | 1075 |
| Asian | 215 |
| Native | 3569 |
| Hispanic/Latino | 2495 |
| Bachelor's or higher | 8267 |

## Districts

- [OK-02](/us/states/ok/districts/02.md) — 100% (congressional)
- [OK Senate District 7](/us/states/ok/districts/senate/7.md) — 100% (state senate)
- [OK House District 17](/us/states/ok/districts/house/17.md) — 62% (state house)
- [OK House District 18](/us/states/ok/districts/house/18.md) — 35% (state house)
- [OK House District 15](/us/states/ok/districts/house/15.md) — 3% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
