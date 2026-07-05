---
type: Jurisdiction
title: "Houston County, GA"
classification: county
fips: "13153"
state: "GA"
demographics:
  population: 169649
  population_under_18: 43325
  population_18_64: 103063
  population_65_plus: 23261
  median_household_income: 80698
  poverty_rate: 11.06
  homeownership_rate: 66.93
  unemployment_rate: 5.1
  median_home_value: 219800
  gini_index: 0.4151
  vacancy_rate: 8.55
  race_white: 91060
  race_black: 55017
  race_asian: 5105
  race_native: 499
  hispanic: 12872
  bachelors_plus: 51843
districts:
  - to: "us/states/ga/districts/08"
    rel: in-district
    area_weight: 0.8691
  - to: "us/states/ga/districts/02"
    rel: in-district
    area_weight: 0.1309
  - to: "us/states/ga/districts/senate/20"
    rel: in-district
    area_weight: 0.8206
  - to: "us/states/ga/districts/senate/26"
    rel: in-district
    area_weight: 0.1202
  - to: "us/states/ga/districts/senate/18"
    rel: in-district
    area_weight: 0.0592
  - to: "us/states/ga/districts/house/148"
    rel: in-district
    area_weight: 0.5986
  - to: "us/states/ga/districts/house/146"
    rel: in-district
    area_weight: 0.225
  - to: "us/states/ga/districts/house/143"
    rel: in-district
    area_weight: 0.103
  - to: "us/states/ga/districts/house/147"
    rel: in-district
    area_weight: 0.0729
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Houston County, GA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 169649 |
| Under 18 | 43325 |
| 18–64 | 103063 |
| 65+ | 23261 |
| Median household income | 80698 |
| Poverty rate | 11.06 |
| Homeownership rate | 66.93 |
| Unemployment rate | 5.1 |
| Median home value | 219800 |
| Gini index | 0.4151 |
| Vacancy rate | 8.55 |
| White | 91060 |
| Black | 55017 |
| Asian | 5105 |
| Native | 499 |
| Hispanic/Latino | 12872 |
| Bachelor's or higher | 51843 |

## Districts

- [GA-08](/us/states/ga/districts/08.md) — 87% (congressional)
- [GA-02](/us/states/ga/districts/02.md) — 13% (congressional)
- [GA Senate District 20](/us/states/ga/districts/senate/20.md) — 82% (state senate)
- [GA Senate District 26](/us/states/ga/districts/senate/26.md) — 12% (state senate)
- [GA Senate District 18](/us/states/ga/districts/senate/18.md) — 6% (state senate)
- [GA House District 148](/us/states/ga/districts/house/148.md) — 60% (state house)
- [GA House District 146](/us/states/ga/districts/house/146.md) — 22% (state house)
- [GA House District 143](/us/states/ga/districts/house/143.md) — 10% (state house)
- [GA House District 147](/us/states/ga/districts/house/147.md) — 7% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
