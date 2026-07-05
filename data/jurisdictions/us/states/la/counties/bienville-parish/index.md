---
type: Jurisdiction
title: "Bienville Parish, LA"
classification: county
fips: "22013"
state: "LA"
demographics:
  population: 12638
  population_under_18: 2860
  population_18_64: 7084
  population_65_plus: 2694
  median_household_income: 35011
  poverty_rate: 29.25
  homeownership_rate: 70.21
  unemployment_rate: 6.27
  median_home_value: 99500
  gini_index: 0.5417
  vacancy_rate: 19.31
  race_white: 6932
  race_black: 5098
  race_asian: 28
  race_native: 30
  hispanic: 288
  bachelors_plus: 1417
districts:
  - to: "us/states/la/districts/04"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/la/districts/senate/31"
    rel: in-district
    area_weight: 0.6623
  - to: "us/states/la/districts/senate/29"
    rel: in-district
    area_weight: 0.3109
  - to: "us/states/la/districts/senate/33"
    rel: in-district
    area_weight: 0.0265
  - to: "us/states/la/districts/house/13"
    rel: in-district
    area_weight: 0.8354
  - to: "us/states/la/districts/house/11"
    rel: in-district
    area_weight: 0.1645
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, la]
timestamp: "2026-07-03"
---

# Bienville Parish, LA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 12638 |
| Under 18 | 2860 |
| 18–64 | 7084 |
| 65+ | 2694 |
| Median household income | 35011 |
| Poverty rate | 29.25 |
| Homeownership rate | 70.21 |
| Unemployment rate | 6.27 |
| Median home value | 99500 |
| Gini index | 0.5417 |
| Vacancy rate | 19.31 |
| White | 6932 |
| Black | 5098 |
| Asian | 28 |
| Native | 30 |
| Hispanic/Latino | 288 |
| Bachelor's or higher | 1417 |

## Districts

- [LA-04](/us/states/la/districts/04.md) — 100% (congressional)
- [LA Senate District 31](/us/states/la/districts/senate/31.md) — 66% (state senate)
- [LA Senate District 29](/us/states/la/districts/senate/29.md) — 31% (state senate)
- [LA Senate District 33](/us/states/la/districts/senate/33.md) — 3% (state senate)
- [LA House District 13](/us/states/la/districts/house/13.md) — 84% (state house)
- [LA House District 11](/us/states/la/districts/house/11.md) — 16% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
