---
type: Jurisdiction
title: "Morris County, KS"
classification: county
fips: "20127"
state: "KS"
demographics:
  population: 5340
  population_under_18: 1103
  population_18_64: 2852
  population_65_plus: 1385
  median_household_income: 58686
  poverty_rate: 12.06
  homeownership_rate: 80.12
  unemployment_rate: 2.49
  median_home_value: 129600
  gini_index: 0.4386
  vacancy_rate: 14.86
  race_white: 4872
  race_black: 2
  race_asian: 37
  race_native: 0
  hispanic: 232
  bachelors_plus: 1516
districts:
  - to: "us/states/ks/districts/02"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ks/districts/senate/17"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ks/districts/house/68"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ks]
timestamp: "2026-07-03"
---

# Morris County, KS

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 5340 |
| Under 18 | 1103 |
| 18–64 | 2852 |
| 65+ | 1385 |
| Median household income | 58686 |
| Poverty rate | 12.06 |
| Homeownership rate | 80.12 |
| Unemployment rate | 2.49 |
| Median home value | 129600 |
| Gini index | 0.4386 |
| Vacancy rate | 14.86 |
| White | 4872 |
| Black | 2 |
| Asian | 37 |
| Native | 0 |
| Hispanic/Latino | 232 |
| Bachelor's or higher | 1516 |

## Districts

- [KS-02](/us/states/ks/districts/02.md) — 100% (congressional)
- [KS Senate District 17](/us/states/ks/districts/senate/17.md) — 100% (state senate)
- [KS House District 68](/us/states/ks/districts/house/68.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
