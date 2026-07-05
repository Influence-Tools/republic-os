---
type: Jurisdiction
title: "Clarke County, AL"
classification: county
fips: "01025"
state: "AL"
demographics:
  population: 22543
  population_under_18: 4858
  population_18_64: 12937
  population_65_plus: 4748
  median_household_income: 49249
  poverty_rate: 20.06
  homeownership_rate: 70.78
  unemployment_rate: 9.19
  median_home_value: 121700
  gini_index: 0.5318
  vacancy_rate: 28.31
  race_white: 11586
  race_black: 10069
  race_asian: 119
  race_native: 35
  hispanic: 275
  bachelors_plus: 3160
districts:
  - to: "us/states/al/districts/07"
    rel: in-district
    area_weight: 0.6757
  - to: "us/states/al/districts/02"
    rel: in-district
    area_weight: 0.323
  - to: "us/states/al/districts/senate/23"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/al/districts/house/65"
    rel: in-district
    area_weight: 0.5102
  - to: "us/states/al/districts/house/68"
    rel: in-district
    area_weight: 0.4898
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, al]
timestamp: "2026-07-03"
---

# Clarke County, AL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 22543 |
| Under 18 | 4858 |
| 18–64 | 12937 |
| 65+ | 4748 |
| Median household income | 49249 |
| Poverty rate | 20.06 |
| Homeownership rate | 70.78 |
| Unemployment rate | 9.19 |
| Median home value | 121700 |
| Gini index | 0.5318 |
| Vacancy rate | 28.31 |
| White | 11586 |
| Black | 10069 |
| Asian | 119 |
| Native | 35 |
| Hispanic/Latino | 275 |
| Bachelor's or higher | 3160 |

## Districts

- [AL-07](/us/states/al/districts/07.md) — 68% (congressional)
- [AL-02](/us/states/al/districts/02.md) — 32% (congressional)
- [AL Senate District 23](/us/states/al/districts/senate/23.md) — 100% (state senate)
- [AL House District 65](/us/states/al/districts/house/65.md) — 51% (state house)
- [AL House District 68](/us/states/al/districts/house/68.md) — 49% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
