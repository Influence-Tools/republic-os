---
type: Jurisdiction
title: "Putnam County, IL"
classification: county
fips: "17155"
state: "IL"
demographics:
  population: 5601
  population_under_18: 1103
  population_18_64: 3119
  population_65_plus: 1379
  median_household_income: 75590
  poverty_rate: 8.09
  homeownership_rate: 81.46
  unemployment_rate: 4.17
  median_home_value: 172700
  gini_index: 0.3954
  vacancy_rate: 20.23
  race_white: 5113
  race_black: 19
  race_asian: 42
  race_native: 2
  hispanic: 368
  bachelors_plus: 1280
districts:
  - to: "us/states/il/districts/16"
    rel: in-district
    area_weight: 0.5745
  - to: "us/states/il/districts/14"
    rel: in-district
    area_weight: 0.4255
  - to: "us/states/il/districts/senate/53"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/il/districts/house/105"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, il]
timestamp: "2026-07-03"
---

# Putnam County, IL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 5601 |
| Under 18 | 1103 |
| 18–64 | 3119 |
| 65+ | 1379 |
| Median household income | 75590 |
| Poverty rate | 8.09 |
| Homeownership rate | 81.46 |
| Unemployment rate | 4.17 |
| Median home value | 172700 |
| Gini index | 0.3954 |
| Vacancy rate | 20.23 |
| White | 5113 |
| Black | 19 |
| Asian | 42 |
| Native | 2 |
| Hispanic/Latino | 368 |
| Bachelor's or higher | 1280 |

## Districts

- [IL-16](/us/states/il/districts/16.md) — 57% (congressional)
- [IL-14](/us/states/il/districts/14.md) — 43% (congressional)
- [IL Senate District 53](/us/states/il/districts/senate/53.md) — 100% (state senate)
- [IL House District 105](/us/states/il/districts/house/105.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
