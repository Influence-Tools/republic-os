---
type: Jurisdiction
title: "Monroe County, AL"
classification: county
fips: "01099"
state: "AL"
demographics:
  population: 19388
  population_under_18: 4101
  population_18_64: 11093
  population_65_plus: 4194
  median_household_income: 42292
  poverty_rate: 20.09
  homeownership_rate: 71.71
  unemployment_rate: 10.37
  median_home_value: 120600
  gini_index: 0.4578
  vacancy_rate: 27.87
  race_white: 10390
  race_black: 8127
  race_asian: 73
  race_native: 169
  hispanic: 45
  bachelors_plus: 2293
districts:
  - to: "us/states/al/districts/02"
    rel: in-district
    area_weight: 0.9988
  - to: "us/states/al/districts/senate/23"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/al/districts/house/68"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, al]
timestamp: "2026-07-03"
---

# Monroe County, AL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 19388 |
| Under 18 | 4101 |
| 18–64 | 11093 |
| 65+ | 4194 |
| Median household income | 42292 |
| Poverty rate | 20.09 |
| Homeownership rate | 71.71 |
| Unemployment rate | 10.37 |
| Median home value | 120600 |
| Gini index | 0.4578 |
| Vacancy rate | 27.87 |
| White | 10390 |
| Black | 8127 |
| Asian | 73 |
| Native | 169 |
| Hispanic/Latino | 45 |
| Bachelor's or higher | 2293 |

## Districts

- [AL-02](/us/states/al/districts/02.md) — 100% (congressional)
- [AL Senate District 23](/us/states/al/districts/senate/23.md) — 100% (state senate)
- [AL House District 68](/us/states/al/districts/house/68.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
