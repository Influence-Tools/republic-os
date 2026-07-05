---
type: Jurisdiction
title: "Gloucester County, NJ"
classification: county
fips: "34015"
state: "NJ"
demographics:
  population: 306954
  population_under_18: 65238
  population_18_64: 189849
  population_65_plus: 51867
  median_household_income: 105115
  poverty_rate: 7.7
  homeownership_rate: 80.12
  unemployment_rate: 5.27
  median_home_value: 310400
  gini_index: 0.4192
  vacancy_rate: 4.55
  race_white: 232690
  race_black: 33266
  race_asian: 9702
  race_native: 515
  hispanic: 25470
  bachelors_plus: 104720
districts:
  - to: "us/states/nj/districts/02"
    rel: in-district
    area_weight: 0.5625
  - to: "us/states/nj/districts/01"
    rel: in-district
    area_weight: 0.4369
  - to: "us/states/nj/districts/senate/3"
    rel: in-district
    area_weight: 0.5619
  - to: "us/states/nj/districts/senate/4"
    rel: in-district
    area_weight: 0.3756
  - to: "us/states/nj/districts/senate/5"
    rel: in-district
    area_weight: 0.0622
  - to: "us/states/nj/districts/house/3"
    rel: in-district
    area_weight: 0.5619
  - to: "us/states/nj/districts/house/4"
    rel: in-district
    area_weight: 0.3756
  - to: "us/states/nj/districts/house/5"
    rel: in-district
    area_weight: 0.0622
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nj]
timestamp: "2026-07-03"
---

# Gloucester County, NJ

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 306954 |
| Under 18 | 65238 |
| 18–64 | 189849 |
| 65+ | 51867 |
| Median household income | 105115 |
| Poverty rate | 7.7 |
| Homeownership rate | 80.12 |
| Unemployment rate | 5.27 |
| Median home value | 310400 |
| Gini index | 0.4192 |
| Vacancy rate | 4.55 |
| White | 232690 |
| Black | 33266 |
| Asian | 9702 |
| Native | 515 |
| Hispanic/Latino | 25470 |
| Bachelor's or higher | 104720 |

## Districts

- [NJ-02](/us/states/nj/districts/02.md) — 56% (congressional)
- [NJ-01](/us/states/nj/districts/01.md) — 44% (congressional)
- [NJ Senate District 3](/us/states/nj/districts/senate/3.md) — 56% (state senate)
- [NJ Senate District 4](/us/states/nj/districts/senate/4.md) — 38% (state senate)
- [NJ Senate District 5](/us/states/nj/districts/senate/5.md) — 6% (state senate)
- [NJ House District 3](/us/states/nj/districts/house/3.md) — 56% (state house)
- [NJ House District 4](/us/states/nj/districts/house/4.md) — 38% (state house)
- [NJ House District 5](/us/states/nj/districts/house/5.md) — 6% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
