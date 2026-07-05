---
type: Jurisdiction
title: "Coffee County, AL"
classification: county
fips: "01031"
state: "AL"
demographics:
  population: 54920
  population_under_18: 13250
  population_18_64: 32224
  population_65_plus: 9446
  median_household_income: 68353
  poverty_rate: 16.71
  homeownership_rate: 72.26
  unemployment_rate: 5.09
  median_home_value: 188600
  gini_index: 0.4458
  vacancy_rate: 14.89
  race_white: 39036
  race_black: 8909
  race_asian: 631
  race_native: 343
  hispanic: 5396
  bachelors_plus: 12167
districts:
  - to: "us/states/al/districts/01"
    rel: in-district
    area_weight: 0.999
  - to: "us/states/al/districts/senate/31"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/al/districts/house/91"
    rel: in-district
    area_weight: 0.5799
  - to: "us/states/al/districts/house/90"
    rel: in-district
    area_weight: 0.2453
  - to: "us/states/al/districts/house/92"
    rel: in-district
    area_weight: 0.1747
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, al]
timestamp: "2026-07-03"
---

# Coffee County, AL

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 54920 |
| Under 18 | 13250 |
| 18–64 | 32224 |
| 65+ | 9446 |
| Median household income | 68353 |
| Poverty rate | 16.71 |
| Homeownership rate | 72.26 |
| Unemployment rate | 5.09 |
| Median home value | 188600 |
| Gini index | 0.4458 |
| Vacancy rate | 14.89 |
| White | 39036 |
| Black | 8909 |
| Asian | 631 |
| Native | 343 |
| Hispanic/Latino | 5396 |
| Bachelor's or higher | 12167 |

## Districts

- [AL-01](/us/states/al/districts/01.md) — 100% (congressional)
- [AL Senate District 31](/us/states/al/districts/senate/31.md) — 100% (state senate)
- [AL House District 91](/us/states/al/districts/house/91.md) — 58% (state house)
- [AL House District 90](/us/states/al/districts/house/90.md) — 25% (state house)
- [AL House District 92](/us/states/al/districts/house/92.md) — 17% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
