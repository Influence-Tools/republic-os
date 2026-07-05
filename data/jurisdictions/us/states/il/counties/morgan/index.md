---
type: Jurisdiction
title: "Morgan County, IL"
classification: county
fips: "17137"
state: "IL"
demographics:
  population: 33021
  population_under_18: 6252
  population_18_64: 19872
  population_65_plus: 6897
  median_household_income: 66306
  poverty_rate: 13.42
  homeownership_rate: 72.75
  unemployment_rate: 5.38
  median_home_value: 130800
  gini_index: 0.4459
  vacancy_rate: 12.92
  race_white: 28951
  race_black: 1619
  race_asian: 276
  race_native: 45
  hispanic: 967
  bachelors_plus: 6794
districts:
  - to: "us/states/il/districts/15"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/il/districts/senate/50"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/il/districts/house/99"
    rel: in-district
    area_weight: 0.5898
  - to: "us/states/il/districts/house/100"
    rel: in-district
    area_weight: 0.4102
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, il]
timestamp: "2026-07-03"
---

# Morgan County, IL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 33021 |
| Under 18 | 6252 |
| 18–64 | 19872 |
| 65+ | 6897 |
| Median household income | 66306 |
| Poverty rate | 13.42 |
| Homeownership rate | 72.75 |
| Unemployment rate | 5.38 |
| Median home value | 130800 |
| Gini index | 0.4459 |
| Vacancy rate | 12.92 |
| White | 28951 |
| Black | 1619 |
| Asian | 276 |
| Native | 45 |
| Hispanic/Latino | 967 |
| Bachelor's or higher | 6794 |

## Districts

- [IL-15](/us/states/il/districts/15.md) — 100% (congressional)
- [IL Senate District 50](/us/states/il/districts/senate/50.md) — 100% (state senate)
- [IL House District 99](/us/states/il/districts/house/99.md) — 59% (state house)
- [IL House District 100](/us/states/il/districts/house/100.md) — 41% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
