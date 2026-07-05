---
type: Jurisdiction
title: "Woods County, OK"
classification: county
fips: "40151"
state: "OK"
demographics:
  population: 8596
  population_under_18: 1790
  population_18_64: 5305
  population_65_plus: 1501
  median_household_income: 53275
  poverty_rate: 19.88
  homeownership_rate: 65.26
  unemployment_rate: 4.65
  median_home_value: 139600
  gini_index: 0.4456
  vacancy_rate: 19.41
  race_white: 7392
  race_black: 229
  race_asian: 3
  race_native: 234
  hispanic: 641
  bachelors_plus: 2328
districts:
  - to: "us/states/ok/districts/03"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ok/districts/senate/27"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ok/districts/house/58"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ok]
timestamp: "2026-07-03"
---

# Woods County, OK

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 8596 |
| Under 18 | 1790 |
| 18–64 | 5305 |
| 65+ | 1501 |
| Median household income | 53275 |
| Poverty rate | 19.88 |
| Homeownership rate | 65.26 |
| Unemployment rate | 4.65 |
| Median home value | 139600 |
| Gini index | 0.4456 |
| Vacancy rate | 19.41 |
| White | 7392 |
| Black | 229 |
| Asian | 3 |
| Native | 234 |
| Hispanic/Latino | 641 |
| Bachelor's or higher | 2328 |

## Districts

- [OK-03](/us/states/ok/districts/03.md) — 100% (congressional)
- [OK Senate District 27](/us/states/ok/districts/senate/27.md) — 100% (state senate)
- [OK House District 58](/us/states/ok/districts/house/58.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
