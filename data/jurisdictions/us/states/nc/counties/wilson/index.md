---
type: Jurisdiction
title: "Wilson County, NC"
classification: county
fips: "37195"
state: "NC"
demographics:
  population: 79290
  population_under_18: 18060
  population_18_64: 45934
  population_65_plus: 15296
  median_household_income: 56423
  poverty_rate: 19.8
  homeownership_rate: 60.05
  unemployment_rate: 5.63
  median_home_value: 186000
  gini_index: 0.4746
  vacancy_rate: 10.75
  race_white: 36124
  race_black: 30773
  race_asian: 910
  race_native: 219
  hispanic: 9830
  bachelors_plus: 16257
districts:
  - to: "us/states/nc/districts/01"
    rel: in-district
    area_weight: 0.9991
  - to: "us/states/nc/districts/senate/4"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/nc/districts/house/24"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nc]
timestamp: "2026-07-03"
---

# Wilson County, NC

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 79290 |
| Under 18 | 18060 |
| 18–64 | 45934 |
| 65+ | 15296 |
| Median household income | 56423 |
| Poverty rate | 19.8 |
| Homeownership rate | 60.05 |
| Unemployment rate | 5.63 |
| Median home value | 186000 |
| Gini index | 0.4746 |
| Vacancy rate | 10.75 |
| White | 36124 |
| Black | 30773 |
| Asian | 910 |
| Native | 219 |
| Hispanic/Latino | 9830 |
| Bachelor's or higher | 16257 |

## Districts

- [NC-01](/us/states/nc/districts/01.md) — 100% (congressional)
- [NC Senate District 4](/us/states/nc/districts/senate/4.md) — 100% (state senate)
- [NC House District 24](/us/states/nc/districts/house/24.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
