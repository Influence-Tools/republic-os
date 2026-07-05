---
type: Jurisdiction
title: "Cortland County, NY"
classification: county
fips: "36023"
state: "NY"
demographics:
  population: 46246
  population_under_18: 8547
  population_18_64: 29770
  population_65_plus: 7929
  median_household_income: 70418
  poverty_rate: 12.76
  homeownership_rate: 66.3
  unemployment_rate: 4.58
  median_home_value: 162100
  gini_index: 0.4184
  vacancy_rate: 8.84
  race_white: 41609
  race_black: 861
  race_asian: 656
  race_native: 27
  hispanic: 1666
  bachelors_plus: 12589
districts:
  - to: "us/states/ny/districts/19"
    rel: in-district
    area_weight: 0.5163
  - to: "us/states/ny/districts/22"
    rel: in-district
    area_weight: 0.4837
  - to: "us/states/ny/districts/senate/52"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ny/districts/house/131"
    rel: in-district
    area_weight: 0.7001
  - to: "us/states/ny/districts/house/125"
    rel: in-district
    area_weight: 0.2999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ny]
timestamp: "2026-07-03"
---

# Cortland County, NY

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 46246 |
| Under 18 | 8547 |
| 18–64 | 29770 |
| 65+ | 7929 |
| Median household income | 70418 |
| Poverty rate | 12.76 |
| Homeownership rate | 66.3 |
| Unemployment rate | 4.58 |
| Median home value | 162100 |
| Gini index | 0.4184 |
| Vacancy rate | 8.84 |
| White | 41609 |
| Black | 861 |
| Asian | 656 |
| Native | 27 |
| Hispanic/Latino | 1666 |
| Bachelor's or higher | 12589 |

## Districts

- [NY-19](/us/states/ny/districts/19.md) — 52% (congressional)
- [NY-22](/us/states/ny/districts/22.md) — 48% (congressional)
- [NY Senate District 52](/us/states/ny/districts/senate/52.md) — 100% (state senate)
- [NY House District 131](/us/states/ny/districts/house/131.md) — 70% (state house)
- [NY House District 125](/us/states/ny/districts/house/125.md) — 30% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
