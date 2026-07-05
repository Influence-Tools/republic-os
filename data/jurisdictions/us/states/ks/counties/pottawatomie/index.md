---
type: Jurisdiction
title: "Pottawatomie County, KS"
classification: county
fips: "20149"
state: "KS"
demographics:
  population: 26204
  population_under_18: 7557
  population_18_64: 14627
  population_65_plus: 4020
  median_household_income: 92325
  poverty_rate: 6.66
  homeownership_rate: 82.22
  unemployment_rate: 2.14
  median_home_value: 245900
  gini_index: 0.3855
  vacancy_rate: 8.16
  race_white: 23362
  race_black: 434
  race_asian: 112
  race_native: 105
  hispanic: 1590
  bachelors_plus: 8711
districts:
  - to: "us/states/ks/districts/01"
    rel: in-district
    area_weight: 0.998
  - to: "us/states/ks/districts/senate/18"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/ks/districts/house/61"
    rel: in-district
    area_weight: 0.9531
  - to: "us/states/ks/districts/house/51"
    rel: in-district
    area_weight: 0.0468
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ks]
timestamp: "2026-07-03"
---

# Pottawatomie County, KS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 26204 |
| Under 18 | 7557 |
| 18–64 | 14627 |
| 65+ | 4020 |
| Median household income | 92325 |
| Poverty rate | 6.66 |
| Homeownership rate | 82.22 |
| Unemployment rate | 2.14 |
| Median home value | 245900 |
| Gini index | 0.3855 |
| Vacancy rate | 8.16 |
| White | 23362 |
| Black | 434 |
| Asian | 112 |
| Native | 105 |
| Hispanic/Latino | 1590 |
| Bachelor's or higher | 8711 |

## Districts

- [KS-01](/us/states/ks/districts/01.md) — 100% (congressional)
- [KS Senate District 18](/us/states/ks/districts/senate/18.md) — 100% (state senate)
- [KS House District 61](/us/states/ks/districts/house/61.md) — 95% (state house)
- [KS House District 51](/us/states/ks/districts/house/51.md) — 5% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
