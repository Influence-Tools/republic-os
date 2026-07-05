---
type: Jurisdiction
title: "Lyon County, KS"
classification: county
fips: "20111"
state: "KS"
demographics:
  population: 32186
  population_under_18: 7133
  population_18_64: 19857
  population_65_plus: 5196
  median_household_income: 59912
  poverty_rate: 14.63
  homeownership_rate: 57.87
  unemployment_rate: 1.99
  median_home_value: 150600
  gini_index: 0.4088
  vacancy_rate: 10.29
  race_white: 23027
  race_black: 452
  race_asian: 665
  race_native: 149
  hispanic: 7780
  bachelors_plus: 7300
districts:
  - to: "us/states/ks/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ks/districts/senate/17"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ks/districts/house/76"
    rel: in-district
    area_weight: 0.6679
  - to: "us/states/ks/districts/house/13"
    rel: in-district
    area_weight: 0.1891
  - to: "us/states/ks/districts/house/60"
    rel: in-district
    area_weight: 0.143
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ks]
timestamp: "2026-07-03"
---

# Lyon County, KS

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 32186 |
| Under 18 | 7133 |
| 18–64 | 19857 |
| 65+ | 5196 |
| Median household income | 59912 |
| Poverty rate | 14.63 |
| Homeownership rate | 57.87 |
| Unemployment rate | 1.99 |
| Median home value | 150600 |
| Gini index | 0.4088 |
| Vacancy rate | 10.29 |
| White | 23027 |
| Black | 452 |
| Asian | 665 |
| Native | 149 |
| Hispanic/Latino | 7780 |
| Bachelor's or higher | 7300 |

## Districts

- [KS-02](/us/states/ks/districts/02.md) — 100% (congressional)
- [KS Senate District 17](/us/states/ks/districts/senate/17.md) — 100% (state senate)
- [KS House District 76](/us/states/ks/districts/house/76.md) — 67% (state house)
- [KS House District 13](/us/states/ks/districts/house/13.md) — 19% (state house)
- [KS House District 60](/us/states/ks/districts/house/60.md) — 14% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
