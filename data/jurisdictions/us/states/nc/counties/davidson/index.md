---
type: Jurisdiction
title: "Davidson County, NC"
classification: county
fips: "37057"
state: "NC"
demographics:
  population: 172954
  population_under_18: 37476
  population_18_64: 102580
  population_65_plus: 32898
  median_household_income: 64172
  poverty_rate: 12.85
  homeownership_rate: 74.37
  unemployment_rate: 4.08
  median_home_value: 219100
  gini_index: 0.441
  vacancy_rate: 8.57
  race_white: 133972
  race_black: 16096
  race_asian: 2667
  race_native: 373
  hispanic: 15456
  bachelors_plus: 34779
districts:
  - to: "us/states/nc/districts/06"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/nc/districts/senate/30"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/nc/districts/house/80"
    rel: in-district
    area_weight: 0.53
  - to: "us/states/nc/districts/house/81"
    rel: in-district
    area_weight: 0.4698
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nc]
timestamp: "2026-07-03"
---

# Davidson County, NC

County jurisdiction — 5 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 172954 |
| Under 18 | 37476 |
| 18–64 | 102580 |
| 65+ | 32898 |
| Median household income | 64172 |
| Poverty rate | 12.85 |
| Homeownership rate | 74.37 |
| Unemployment rate | 4.08 |
| Median home value | 219100 |
| Gini index | 0.441 |
| Vacancy rate | 8.57 |
| White | 133972 |
| Black | 16096 |
| Asian | 2667 |
| Native | 373 |
| Hispanic/Latino | 15456 |
| Bachelor's or higher | 34779 |

## Districts

- [NC-06](/us/states/nc/districts/06.md) — 100% (congressional)
- [NC Senate District 30](/us/states/nc/districts/senate/30.md) — 100% (state senate)
- [NC House District 80](/us/states/nc/districts/house/80.md) — 53% (state house)
- [NC House District 81](/us/states/nc/districts/house/81.md) — 47% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
