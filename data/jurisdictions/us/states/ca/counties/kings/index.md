---
type: Jurisdiction
title: "Kings County, CA"
classification: county
fips: "06031"
state: "CA"
demographics:
  population: 153298
  population_under_18: 41126
  population_18_64: 95588
  population_65_plus: 16584
  median_household_income: 70995
  poverty_rate: 15.98
  homeownership_rate: 54.19
  unemployment_rate: 10.8
  median_home_value: 324300
  gini_index: 0.42
  vacancy_rate: 6.24
  race_white: 58349
  race_black: 9453
  race_asian: 5792
  race_native: 3316
  hispanic: 89248
  bachelors_plus: 17298
districts:
  - to: "us/states/ca/districts/22"
    rel: in-district
    area_weight: 0.8269
  - to: "us/states/ca/districts/20"
    rel: in-district
    area_weight: 0.1724
  - to: "us/states/ca/districts/senate/16"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ca/districts/house/33"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ca]
timestamp: "2026-07-03"
---

# Kings County, CA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 153298 |
| Under 18 | 41126 |
| 18–64 | 95588 |
| 65+ | 16584 |
| Median household income | 70995 |
| Poverty rate | 15.98 |
| Homeownership rate | 54.19 |
| Unemployment rate | 10.8 |
| Median home value | 324300 |
| Gini index | 0.42 |
| Vacancy rate | 6.24 |
| White | 58349 |
| Black | 9453 |
| Asian | 5792 |
| Native | 3316 |
| Hispanic/Latino | 89248 |
| Bachelor's or higher | 17298 |

## Districts

- [CA-22](/us/states/ca/districts/22.md) — 83% (congressional)
- [CA-20](/us/states/ca/districts/20.md) — 17% (congressional)
- [CA Senate District 16](/us/states/ca/districts/senate/16.md) — 100% (state senate)
- [CA House District 33](/us/states/ca/districts/house/33.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
