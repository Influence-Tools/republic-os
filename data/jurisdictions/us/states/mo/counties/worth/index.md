---
type: Jurisdiction
title: "Worth County, MO"
classification: county
fips: "29227"
state: "MO"
demographics:
  population: 1934
  population_under_18: 418
  population_18_64: 1006
  population_65_plus: 510
  median_household_income: 47847
  poverty_rate: 20.56
  homeownership_rate: 82.05
  unemployment_rate: 1.56
  median_home_value: 96600
  gini_index: 0.4314
  vacancy_rate: 24.1
  race_white: 1842
  race_black: 2
  race_asian: 0
  race_native: 4
  hispanic: 12
  bachelors_plus: 404
districts:
  - to: "us/states/mo/districts/06"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/mo/districts/senate/12"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/mo/districts/house/2"
    rel: in-district
    area_weight: 0.9993
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mo]
timestamp: "2026-07-03"
---

# Worth County, MO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 1934 |
| Under 18 | 418 |
| 18–64 | 1006 |
| 65+ | 510 |
| Median household income | 47847 |
| Poverty rate | 20.56 |
| Homeownership rate | 82.05 |
| Unemployment rate | 1.56 |
| Median home value | 96600 |
| Gini index | 0.4314 |
| Vacancy rate | 24.1 |
| White | 1842 |
| Black | 2 |
| Asian | 0 |
| Native | 4 |
| Hispanic/Latino | 12 |
| Bachelor's or higher | 404 |

## Districts

- [MO-06](/us/states/mo/districts/06.md) — 100% (congressional)
- [MO Senate District 12](/us/states/mo/districts/senate/12.md) — 100% (state senate)
- [MO House District 2](/us/states/mo/districts/house/2.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
