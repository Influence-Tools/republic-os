---
type: Jurisdiction
title: "Bedford County, PA"
classification: county
fips: "42009"
state: "PA"
demographics:
  population: 47513
  population_under_18: 9234
  population_18_64: 26888
  population_65_plus: 11391
  median_household_income: 59992
  poverty_rate: 11.55
  homeownership_rate: 77.54
  unemployment_rate: 3.91
  median_home_value: 179000
  gini_index: 0.4308
  vacancy_rate: 16.2
  race_white: 45397
  race_black: 342
  race_asian: 247
  race_native: 31
  hispanic: 644
  bachelors_plus: 7621
districts:
  - to: "us/states/pa/districts/13"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/pa/districts/senate/32"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/pa/districts/house/78"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, pa]
timestamp: "2026-07-03"
---

# Bedford County, PA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 47513 |
| Under 18 | 9234 |
| 18–64 | 26888 |
| 65+ | 11391 |
| Median household income | 59992 |
| Poverty rate | 11.55 |
| Homeownership rate | 77.54 |
| Unemployment rate | 3.91 |
| Median home value | 179000 |
| Gini index | 0.4308 |
| Vacancy rate | 16.2 |
| White | 45397 |
| Black | 342 |
| Asian | 247 |
| Native | 31 |
| Hispanic/Latino | 644 |
| Bachelor's or higher | 7621 |

## Districts

- [PA-13](/us/states/pa/districts/13.md) — 100% (congressional)
- [PA Senate District 32](/us/states/pa/districts/senate/32.md) — 100% (state senate)
- [PA House District 78](/us/states/pa/districts/house/78.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
