---
type: Jurisdiction
title: "Cleburne County, AL"
classification: county
fips: "01029"
state: "AL"
demographics:
  population: 15426
  population_under_18: 3387
  population_18_64: 8936
  population_65_plus: 3103
  median_household_income: 55345
  poverty_rate: 13.68
  homeownership_rate: 78.55
  unemployment_rate: 2.57
  median_home_value: 165600
  gini_index: 0.4441
  vacancy_rate: 13.01
  race_white: 14309
  race_black: 562
  race_asian: 18
  race_native: 48
  hispanic: 325
  bachelors_plus: 2682
districts:
  - to: "us/states/al/districts/03"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/al/districts/senate/13"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/al/districts/house/40"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, al]
timestamp: "2026-07-03"
---

# Cleburne County, AL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 15426 |
| Under 18 | 3387 |
| 18–64 | 8936 |
| 65+ | 3103 |
| Median household income | 55345 |
| Poverty rate | 13.68 |
| Homeownership rate | 78.55 |
| Unemployment rate | 2.57 |
| Median home value | 165600 |
| Gini index | 0.4441 |
| Vacancy rate | 13.01 |
| White | 14309 |
| Black | 562 |
| Asian | 18 |
| Native | 48 |
| Hispanic/Latino | 325 |
| Bachelor's or higher | 2682 |

## Districts

- [AL-03](/us/states/al/districts/03.md) — 100% (congressional)
- [AL Senate District 13](/us/states/al/districts/senate/13.md) — 100% (state senate)
- [AL House District 40](/us/states/al/districts/house/40.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
